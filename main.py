from IPython.display import Markdown
from chat_bot import ChatBot
from prompt_creator import PromptCreator
from api_key import API_KEY

def main():
	chat_bot = ChatBot(API_KEY)
	prompt_creator = PromptCreator()
	template = prompt_creator.create_template()
	prompt = prompt_creator.from_template(template)
	chain = chat_bot.create_chain(prompt)

	question = "질문"
	print(Markdown(chain.invoke({'question': question}).content).data)

if __name__ == "__main__":
	main()