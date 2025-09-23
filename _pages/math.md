---
layout: archive
title: "Mathematical Foundations"
permalink: /math/
author_profile: true
---

<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
  }
};
</script>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

## 🧮 머신러닝 수학 개념 정리

NLP와 LLM 연구에서 핵심적으로 사용되는 수학적 개념들을 정리했습니다.

---

## 1. InfoNCE Loss

**Contrastive Learning**의 핵심 손실 함수로, anchor 샘플과 positive/negative 예시들을 비교합니다.

$$\mathcal{L}_{\text{InfoNCE}} = -\log \frac{\exp(\text{sim}(a, p) / \tau)}{\exp(\text{sim}(a, p) / \tau) + \sum_{i=1}^{N} \exp(\text{sim}(a, n_i) / \tau)}$$

**파라미터 설명**:
- $a$: anchor sample (기준 샘플)
- $p$: positive sample (긍정 샘플)
- $n_i$: negative samples (부정 샘플들)
- $\tau$: temperature parameter (온도 파라미터)
- $\text{sim}(\cdot, \cdot)$: cosine similarity (코사인 유사도)

**핵심 아이디어**: positive pair의 유사도는 높이고, negative pair의 유사도는 낮춘다.

---

## 2. False Negative Mitigation

**잘못 분류된 네거티브 샘플**의 악영향을 줄이는 핵심 기법입니다.

$$w_i = \begin{cases}
\alpha \text{ (where } 0 < \alpha < 1 \text{)} & \text{if } \text{sim}(a, n_i) > \theta \\
1 & \text{otherwise}
\end{cases}$$

**적용 방법**:
- **Threshold 기반**: 유사도가 높은 negative sample의 가중치 감소
- **Margin 전략**: 절대값/백분율 기준으로 false negative 제거
- **배치 크기 효과**: 큰 배치에서 더 효과적

---

## 3. Hard Negative Mining

**어려운 네거티브 샘플**을 선별하여 학습 효율성을 극대화하는 전략입니다.

### Distance-based Filtering
$$\text{HardNeg} = \{n_i \mid \text{sim}(a, n_i) > \text{threshold}\}$$

### Semi-Hard Negative Selection
$$\text{SemiHardNeg} = \{n_i \mid \text{sim}(a, p) < \text{sim}(a, n_i) < \text{sim}(a, p) + \text{margin}\}$$

**Curriculum Learning**: 점진적으로 어려운 샘플들을 학습에 도입

---

## 4. Dual-Encoder Retrieval

**독립적인 인코더**를 사용한 효율적 검색 시스템 구조입니다.

$$\text{score}(q, d) = f_q(q)^T \cdot f_d(d)$$

**장점**:
- $f_q(\cdot)$: query encoder (쿼리 전용)
- $f_d(\cdot)$: document encoder (문서 전용)
- **병렬 처리**: 문서들을 미리 인코딩하여 빠른 검색 가능

---

## 5. LLM Training Loss Functions

### 5.1. Supervised Fine-Tuning (SFT)

**기본적인 언어모델 파인튜닝**을 위한 손실함수입니다.

$$\mathcal{L}_{\text{SFT}} = -\sum_{t=1}^{T} \log p_\theta(y_t | x, y_{<t})$$

**특징**:
- $x$: input prompt (입력 프롬프트)
- $y_t$: target token at time $t$ (시간 $t$의 타겟 토큰)
- **Next Token Prediction**: 다음 토큰을 예측하는 표준 언어모델링

### 5.2. Direct Preference Optimization (DPO)

**Direct Preference Optimization**을 통한 인간 선호도 학습입니다.

$$\mathcal{L}_{\text{DPO}} = -\mathbb{E}_{(x,y_w,y_l) \sim \mathcal{D}} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right]$$

**핵심 구성요소**:
- $y_w$: preferred response (선호 응답)
- $y_l$: non-preferred response (비선호 응답)
- $\pi_\theta$: target model (학습 모델)
- $\pi_{\text{ref}}$: reference model (기준 모델)
- $\beta$: scaling parameter (스케일링 파라미터)

### 5.3. Identity Preference Optimization (IPO)

**DPO의 개선된 버전**으로, 더 안정적인 학습을 제공합니다.

$$\mathcal{L}_{\text{IPO}} = \mathbb{E}_{(x,y_w,y_l) \sim \mathcal{D}} \left[ \left( \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} - \frac{1}{\beta} \right)^2 \right]$$

**장점**:
- **안정성**: 시그모이드 함수 없이 제곱 손실 사용
- **수렴성**: DPO 대비 더 안정적인 수렴 특성

### 5.4. Group Relative Policy Optimization (GRPO)

**그룹 기반 상대적 정책 최적화**로 다중 응답을 동시에 고려합니다.

$$\mathcal{L}_{\text{GRPO}} = -\mathbb{E}_{(x,\{y_i\}) \sim \mathcal{D}} \left[ \sum_{i=1}^{n} r_i \log \frac{\pi_\theta(y_i|x)}{\pi_{\text{ref}}(y_i|x)} \right]$$

**특징**:
- $\{y_i\}$: multiple responses from the same prompt (동일 프롬프트의 다중 응답)
- $r_i$: relative reward for response $i$ (응답 $i$의 상대적 보상)
- **Group Learning**: 여러 응답을 동시에 고려한 학습

---

## 6. GISTEmbedLoss (나의 기여)

**Guide 모델**을 활용한 개선된 임베딩 학습 손실 함수입니다.

$$\mathcal{L}_{\text{GIST}} = \mathcal{L}_{\text{InfoNCE}} + \lambda \cdot \mathcal{L}_{\text{Guide}}$$

**나의 개선사항**:
- **Multiple Negative 지원**: 기존 1:1:1 구조를 1:1:N으로 확장
- **False Negative 완화**: In-batch negative에서 false negative 제거
- **안정성 향상**: 가이드 모델의 지식 증류로 학습 안정화

$$\mathcal{L}_{\text{Guide}} = \text{KL}(\text{Guide}(a, p, \{n_i\}) \parallel \text{Student}(a, p, \{n_i\}))$$

---

## 7. Attention Mechanism

**Transformer의 핵심 메커니즘**입니다.

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**Multi-Head Attention**:
$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h)W^O$$

여기서 각 $\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$

---

## 🎯 수식 데모

간단한 예제로 **코사인 유사도** 계산:

두 벡터 $\mathbf{a} = [1, 2, 3]$, $\mathbf{b} = [4, 5, 6]$에 대해:

$$\text{cosine\_similarity}(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}| \cdot |\mathbf{b}|} = \frac{32}{\sqrt{14} \cdot \sqrt{77}} \approx 0.974$$

이 수학적 기초들이 제가 개발한 SOTA 임베딩 모델들의 핵심이 되었습니다! 🚀