from IPython.display import Markdown
from chat_bot import ChatBot
from prompt_creator import PromptCreator
from config import API_KEY
from config import PDF_DOCUMENT


def main():
	chat_bot = ChatBot(API_KEY, PDF_DOCUMENT)
	prompt_creator = PromptCreator()
	template = prompt_creator.create_template()
	prompt = prompt_creator.from_template(template)
	chain = chat_bot.create_chain(prompt)

	history =[]

	while len(history) < 10:
		question =input("질문을 입력하세요(종료:'exit'): ")
		if question.lower() == 'exit':
			print("대화를 종료합니다")
			return
		history.append(question)
		answer = chain.invoke({'question': question}).content
		print(Markdown(answer).data)
		
		if len(history) ==10:
			print("질문 횟수가 초과되어 대화를 종료합니다")
			print("대화를 더 원하시는 경우 처음부터 재진행됩니다")
			return
	
    
	#print("질문과 답변 기록")
	#for i, (q, a) in enumerate(zip(history, chain.invoke({'question': question}))):
	#	pass
		#print(f"{i+1}. 질문: {q}\n 답변: {a}\n")        

 

if __name__ == "__main__":
	main()