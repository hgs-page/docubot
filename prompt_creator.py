from langchain.prompts import ChatPromptTemplate

 #
class PromptCreator:
	def create_template(self):
		 # 주어진 컨텍스트와 질문을 기반으로 프롬프트 템플릿을 생성하는 메서드
		return """Answer the question as based only on the following context:
		{context}

		Question: {question}
		"""

	def from_template(self, template):
		return ChatPromptTemplate.from_template(template)
