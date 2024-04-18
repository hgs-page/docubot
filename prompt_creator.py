from langchain.prompts import ChatPromptTemplate


class PromptCreator:
	def create_template(self):
		return """Answer the question as based only on the following context:
		{context}

		Question: {question}
		"""

	def from_template(self, template):
		return ChatPromptTemplate.from_template(template)
