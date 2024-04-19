import json

class Logger:
	def __init__(self, file_name:str) -> None:
		self.log = []  # 로그를 저장할 리스트
		self.file_name = file_name  # 로그를 저장할 파일 이름

	def load(self):
		try:
			with open(self.file_name, 'r') as file:
				self.log = json.load(file)
		except FileNotFoundError:
			self.save()

	def save(self):
		if self.file_name:
			with open(self.file_name, 'w') as file:
				json.dump(self.log, file)
		else:
			print("로그 파일이 지정되지 않았습니다. 먼저 open_log 메서드를 사용하여 파일을 열어주세요.")

	def add(self, q: str, a: str):
		self.log.append({
			"question": q,
			"answer": a
		})

	def get(self, index: int):
		if 0 <= index < len(self.log):
				return self.log[index]
		else:
				return None

	def print(self):
		for i, entry in enumerate(self.log, 1):
			print(f"index: {i}")
			for key, value in entry.items():
				print(f"{key}: {value}")
			print("")

	def clear(self):
		self.log = []
		self.save()
