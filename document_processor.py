import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


class DocumentProcessor:
	def __init__(self, api_key):
		self.api_key = api_key

	def set_google_api_key(self):
		if "GOOGLE_API_KEY" not in os.environ:
			os.environ["GOOGLE_API_KEY"] = self.api_key


	def create_vector_db(self):
		loader = PyPDFLoader("content.pdf")
		pages = loader.load_and_split()

		text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
		texts = text_splitter.split_documents(pages)

		model_name = "jhgan/ko-sbert-nli"
		model_kwargs = {'device': 'cpu'}
		encode_kwargs = {'normalize_embeddings': True}
		hf = HuggingFaceEmbeddings(
			model_name=model_name,
			model_kwargs=model_kwargs,
			encode_kwargs=encode_kwargs
		)

		return Chroma.from_documents(texts, hf)