from __future__ import unicode_literals
import frappe

def get_context(context):
    question_list = frappe.get_doc("Review Test","IT")
    context.questions = question_list


    questions_with_answers = []
    for question_median in question_list.get("question"):
                question = frappe.get_doc("Question", question_median.question)
                                
                questions_with_answers.append({
                                "question": question.question,
                                "answer": question.answer
                                })



    context.view=questions_with_answers



   # for question in question_list.question:
    #    question_doc = frappe.get_doc("Question", question.question)
     #   options = [option.answer for option in question_doc.answer]
      #  context.questions.append({
       #     "question": question_doc.question,
        #    "options": options
       # })

   # answer_list=frappe.get_doc=("Question","how")
    #context.answer=answer_list
    #frappe.msgprint(context)

    #answer_list=frappe.get_list("Question",filters={'question':context.question_list.question})
    #context.questions = [] 
    #for question in question_list:
    return context
    # «” ⁄·«„ ··Õ’Ê· ⁄·Ï «·≈Ã«»«  «·„ ⁄·ﬁ… »«·√”∆·… «·„⁄—Ê÷…


@frappe.whitelist()
def save_selected_value():
        doc=frappe.delete_doc("Review Test","CS")
        doc.save()
        frappe.msgprint("done")