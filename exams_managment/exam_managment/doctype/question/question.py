import frappe
from frappe.model.document import Document

class Question(Document):
	def validates(self):
		answers = []
		for answer in self.answer:
			answers.append(answer.answer)
		frappe.msgprint("\n".join(answers))

question = frappe.get_doc("Question", "how")
question.validates()