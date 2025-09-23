---
layout: archive
title: "HuggingFace Portfolio"
permalink: /huggingface/
author_profile: true
---

<div class="notice--primary">
  <h4>🤗 HuggingFace Profile</h4>
  <p><strong><a href="https://huggingface.co/dragonkue" target="_blank">https://huggingface.co/dragonkue</a></strong></p>
  <p>AutoRAG Embedding Benchmark에서 Bi-Encoder와 Cross-Encoder 모두 SOTA 성능을 달성하며 시작된 오픈소스 기여 활동이 현재는 <strong>MTEB-ko-retrieval Leaderboard</strong>에서 종합 1위를 기록하는 성과로 이어졌습니다.</p>
</div>

---

## 🏆 SOTA 모델들

<style>
.model-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.model-card {
  border: 1px solid #e1e8ed;
  border-radius: 8px;
  padding: 1.5rem;
  background: #f8f9fa;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.model-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.model-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.model-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: bold;
  margin-right: 0.5rem;
}

.sota-badge { background: #ff6b6b; color: white; }
.champion-badge { background: #4ecdc4; color: white; }
.reranker-badge { background: #45b7d1; color: white; }

.model-link {
  font-size: 1.1rem;
  font-weight: bold;
  color: #2c5aa0;
  text-decoration: none;
}

.model-link:hover {
  text-decoration: underline;
}

.model-description {
  margin-top: 0.75rem;
  color: #555;
  line-height: 1.4;
}
</style>

<div class="model-grid">
  <div class="model-card">
    <div class="model-header">
      <span class="model-badge sota-badge">🏆 SOTA</span>
    </div>
    <a href="https://huggingface.co/dragonkue/snowflake-arctic-embed-l-v2.0-ko" target="_blank" class="model-link">
      snowflake-arctic-embed-l-v2.0-ko
    </a>
    <p class="model-description">
      임베딩 모델에서 한국어 IR 벤치마크(<strong>MTEB-ko-retrieval Leaderboard</strong>) 종합 SOTA 모델
    </p>
  </div>

  <div class="model-card">
    <div class="model-header">
      <span class="model-badge champion-badge">🎯 AutoRAG Champion</span>
    </div>
    <a href="https://huggingface.co/dragonkue/BGE-m3-ko" target="_blank" class="model-link">
      BGE-m3-ko
    </a>
    <p class="model-description">
      임베딩 모델에서 AutoRAG Embedding 벤치마크에서 SOTA 모델
    </p>
  </div>

  <div class="model-card">
    <div class="model-header">
      <span class="model-badge reranker-badge">🔄 Reranker SOTA</span>
    </div>
    <a href="https://huggingface.co/dragonkue/bge-reranker-v2-m3-ko" target="_blank" class="model-link">
      bge-reranker-v2-m3-ko
    </a>
    <p class="model-description">
      Reranker 모델에서 AutoRAG Embedding 벤치마크에서 SOTA 모델
    </p>
  </div>
</div>

---

## GitHub 기여

### sentence-transformers 라이브러리 개선

**GISTEmbedLoss 네거티브 확장 기여**를 통해 오픈소스 생태계에 기여했습니다.

#### 🎯 GISTEmbedLoss 1차 개선 (Multiple Negative 지원):
- **기존 문제**: GISTEmbedLoss는 [Anchor, Positive, Negative] 형태의 1:1:1 쌍만 학습 가능
- **해결책**: 최근 Bi-Encoder 모델들(E5, BGE, Arctic 등)이 **복수의 하드 네거티브(7~15개)**를 활용하는 추세를 반영
- **구현**: **Multiple Negative 구조를 지원하도록 GISTEmbedLoss 손실 함수 구조 개선**
- **기술적 의의**: Guide 모델을 통한 기존 MNR Loss 대비 **안정적이고 효과적**인 손실함수

<div class="notice--success">
  <h4>GitHub Contribution #1</h4>
  <p><a href="https://github.com/UKPLab/sentence-transformers/pull/2946" target="_blank">🔗 Pull Request #2946</a></p>
</div>

#### 🛠️ GISTEmbedLoss 2차 개선 (NV-Retriever 기반 Margin Filtering):
- **NV-Retriever 논문 참고**: **false negative 필터링을 위한 margin 기반 로직**을 GISTEmbedLoss에 도입
- **차별점**: anchor에 대한 hard negative 추출 시가 아닌 **In-batch negative에서 false negative 제거 방법을 개선**
- **절대값/백분율 기준 margin 전략**으로 false negative 샘플 제거 → 학습 안정성 및 성능 향상
- **배치 사이즈 효과**: 배치 사이즈가 클수록 더 높은 성능 향상 확인
- **성능 개선**: 기존 `CachedGISTEmbedLoss` 대비 향상된 정확도(Cosine Accuracy) 달성

<div class="notice--success">
  <h4>GitHub Contribution #2</h4>
  <p><a href="https://github.com/UKPLab/sentence-transformers/pull/3299" target="_blank">🔗 Pull Request #3299</a></p>
</div>


