from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableMap
from document_processor import DocumentProcessor


class ChatBot:
	def __init__(self, api_key, model="gemini-pro", temperature=0):
		self.api_key = api_key				
		self.document_processor = DocumentProcessor(api_key)
		self.document_processor.set_google_api_key()
		self.model = ChatGoogleGenerativeAI(model=model, temperature=temperature)

	def create_chain(self, prompt):
		vector_db = self.document_processor.create_vector_db()
		retriever = self.get_retriever(vector_db)
		return RunnableMap({
			"context": lambda x: retriever.get_relevant_documents(x['question']),
			"question": lambda x: x['question']
		}) | prompt | self.model
		

	def get_retriever(self, docsearch):
		return docsearch.as_retriever(
			search_type="mmr",
			search_kwargs={'k': 3, 'fetch_k': 10}
		)
