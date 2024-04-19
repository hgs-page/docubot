
# 챗봇 문서 처리 시스템

## 개요
이 저장소는 문서 기반 질의응답을 제공하기 위해 문서 처리 기능과 챗봇 시스템을 통합한 파이썬 응용 프로그램을 포함합니다. 시스템은 문서를 처리하고, 이를 기반으로 벡터 데이터베이스를 생성한 다음, 사용자 질문에 대한 응답을 생성합니다.

## 저장소 구조
- `merge.py`: 모든 기능을 결합한 주 스크립트.
- `.gitignore`: 추적하지 않을 파일 목록을 지정합니다.
- `api_key.py`: 외부 서비스의 API 키를 관리합니다. api는 gemini-pro를 이용한다.
- `chat_bot.py`: 사용자 질문에 대한 응답을 생성하는 챗봇 기능을 구현합니다. temperature은 기본값으로 하고, create_vector_db 메서드를 사용하여 벡터 데이터베이스를 생성합니다. 파이프라인을 구성하고 리트리버 객체를 반환합니다.
- `content.pdf`: 분석 및 질의응답에 사용될 문서.
- `document_processor.py`: 문서를 분할해서 텍스트를 임베딩합니다. 검색을 위한 벡터 데이터베이스를 구축합니다. 텍스트를 벡터로 변환하여 Chroma 객체를 반환합니다.
- `main.py`: 애플리케이션의 메인 진입점. 
- `prompt_creator.py`: 문서 내용에 기반하여 챗봇용 프롬프트를 생성 및 관리합니다.

## 기능
- **문서 로딩 및 분할**: PDF 문서를 로드하고 관리 가능한 섹션으로 분할합니다.
- **벡터 데이터베이스 생성**: 처리된 텍스트에서 벡터 데이터베이스를 구축하여 문서 검색을 지원합니다.
- **질의 응답**: 문서 컨텍스트를 사용하여 사용자 질문에 관련된 응답을 생성합니다.
- **프롬프트 관리**: 문서 내용에 기반하여 동적으로 챗봇의 프롬프트 템플릿을 생성 및 관리합니다.


## 파이썬 패키지
     
    ipython    
    os
    langchain langchain-google-genai langchain-community langchainhub langchain-chroma bs4
    pypdf
    setence-transformers

아직 설치하지 않았다면 pip install 명령어로 설치하세요.

## 실행 방법
1. 필요한 종속성을 설치합니다:
   ```bash
   pip install langchain-community langchain-google-genai IPython
   ```
2. 메인 스크립트를 실행합니다:
   ```bash
   python main.py
   ```
3. 명령줄 프롬프트를 따라 질문을 입력하고 답변을 받습니다.

## 라이선스
이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 추가 라이센스가 필요하지 
않습니다.