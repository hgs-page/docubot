from logger import Logger
from IPython.display import Markdown
from chat_bot import ChatBot
from prompt_creator import PromptCreator
from config import API_KEY
from config import PDF_DOCUMENT

class Main:
	def __init__(self, api_key:str, pdf_document:str) -> None:
		self.logger = Logger("history.json")
		self.chat_bot = ChatBot(api_key, pdf_document)
		self.prompt_creator = PromptCreator()
		self.template = self.prompt_creator.create_template()
		self.prompt = self.prompt_creator.from_template(self.template)
		self.chain = self.chat_bot.create_chain(self.prompt)
		pass
	def run(self):
		self.logger.load()
		while True:
			question = input("질문을 입력하세요(기록 보기: 1, 기록삭제: 2  종료: exit): ")
			if len(question) == 0:
				print("질문을 입력하세요.")
				continue
			if question.lower() == 'exit':
				print("대화를 종료합니다")
				return
			elif question == "1":
				self.logger.print()
			elif question == "2":
				self.logger.clear()
			else:
				try:
					print("처리중...\n")
					answer = self.chain.invoke({'question': question}).content
					print(Markdown(answer).data+"\n")
					self.logger.add(question, answer)
					self.logger.save()
				except:
					print("뭔가 비정상적인 일이 일어났는데, 뭔지는 모르겠네요. 처신하세요!")


if __name__ == "__main__":
	print("실행중...")
	main = Main(API_KEY, PDF_DOCUMENT)
	main.run()