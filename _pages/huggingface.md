---
layout: archive
title: "HuggingFace"
permalink: /huggingface/
author_profile: true
---

## 오픈소스 활동

AutoRAG Embedding Benchmark에서 Bi-Encoder와 Cross-Encoder 모두 SOTA 성능을 보이는 모델을 만들고 공유하는 것을 시작으로 최근에는 **MTEB-ko-retrieval Leaderboard(8가지 한국어 Retrieval 벤치마크)**에 대해 SOTA 성능을 보이는 모델을 공유했습니다.

<div class="notice--info">
  <h4>HuggingFace Profile</h4>
  <p><a href="https://huggingface.co/dragonkue" target="_blank">🤗 https://huggingface.co/dragonkue</a></p>
</div>

---

## 주요 모델

### 1. snowflake-arctic-embed-l-v2.0-ko
<div class="model-card">
  <p><strong>🏆 SOTA Model</strong></p>
  <p><strong>Link</strong>: <a href="https://huggingface.co/dragonkue/snowflake-arctic-embed-l-v2.0-ko" target="_blank">snowflake-arctic-embed-l-v2.0-ko</a></p>
  <p><strong>Description</strong>: 임베딩 모델에서 한국어 IR 벤치마크(<strong>MTEB-ko-retrieval Leaderboard</strong>) 종합 SOTA 모델</p>
</div>

### 2. BGE-m3-ko
<div class="model-card">
  <p><strong>🎯 AutoRAG Champion</strong></p>
  <p><strong>Link</strong>: <a href="https://huggingface.co/dragonkue/BGE-m3-ko" target="_blank">BGE-m3-ko</a></p>
  <p><strong>Description</strong>: 임베딩 모델에서 AutoRAG Embedding 벤치마크에서 SOTA 모델</p>
</div>

### 3. bge-reranker-v2-m3-ko
<div class="model-card">
  <p><strong>🔄 Reranker SOTA</strong></p>
  <p><strong>Link</strong>: <a href="https://huggingface.co/dragonkue/bge-reranker-v2-m3-ko" target="_blank">bge-reranker-v2-m3-ko</a></p>
  <p><strong>Description</strong>: Reranker 모델에서 AutoRAG Embedding 벤치마크에서 SOTA 모델</p>
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

---

## 커뮤니티 활동

### 인스트럭트-한국 2025 1월 Meetup 발표

**날짜**: 2025.01.25

**개요**: 한국어 LLM 벤치마크인 LogicKor 벤치마크를 운영하는 Instruct KR 주최로 LLM과 RAG 등의 자유 주제 발표에 참여. 허깅페이스에 올린 Embedding Benchmark SOTA 모델을 만든 방법론과 기술적 인사이트를 공유했습니다.

이 기여를 통해 더 효과적인 임베딩 모델 학습이 가능해져 한국어 NLP 연구 발전에 기여하고 있습니다.