from langchain.prompts import ChatPromptTemplate


class PromptCreator:
	def create_template(self):
		return ""

	def from_template(self, template):
		return ChatPromptTemplate.from_template(template)
		pass
