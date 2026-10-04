# 룬 소환 시뮬레이터

무기(1개), 방어구(5개, 잠금 후 재소환), 엠블럼(1개) 룬을 뽑는 가챠 시뮬레이터입니다.
빌드 결과는 이미지까지 모두 포함된 HTML 한 파일이라 어디든 정적 호스팅으로 올릴 수 있어요.

## 구조

```
src/index.template.html   화면, 연출, 효과음, 확률 설정 (실제로 수정하는 파일)
runes/*.png               룬 이미지 74개 (파일명 = 룬 이름, 192px 투명 배경)
build.py                  runes/ 이미지를 템플릿에 넣어 dist/index.html 생성
dist/index.html           배포용 단일 파일 (직접 수정하지 말고 build.py로 생성)
```

## 빌드

```
1. pip install pillow
2. python build.py
3. dist/index.html 을 브라우저로 열어 확인
```

## 자주 하는 수정

- 확률: `src/index.template.html` 맨 위 `RUNES` 의 `w` 값. 같은 종류 안에서 w 비율대로 나오고, 0이면 나오지 않음
- 룬 추가: `runes/`에 `룬이름.png` 를 넣고 `RUNES` 에 `{name:'룬이름', cat:'light', w:1}` 추가 (cat: light 빛 / dark 어둠 / dragon 용 / none 무계열)
- 계열 색: `CAT` 의 `rgb` 값
- 대표 이미지(시작 화면): `TYPES` 의 `showcase`

## 규칙 메모

- 방어구 5칸은 서로 중복 없음, 잠근 룬은 재소환 시 다시 나오지 않음, 잠금 개수 제한 없음
- 등급 표기 없음 (전부 전설 단일 등급)
- 효과음은 Web Audio로 코드에서 합성 (외부 음원 파일 없음)
