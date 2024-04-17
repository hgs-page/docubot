from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableMap
from document_processor import DocumentProcessor


class ChatBot:
	def __init__(self, api_key, model="gemini-pro", temperature=0):
		self.api_key = api_key

	def create_chain(self, prompt):
		# code
		pass

	def get_retriever(self, docsearch):
		# code
		pass
