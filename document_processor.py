import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings


class DocumentProcessor:
	def __init__(self, api_key):
		self.api_key = api_key

	def set_google_api_key(self):
		
		pass

	def create_vector_db(self):
		# code
		return 1
