// Copyright (c) 2024, Exam Managment and contributors
// For license information, please see license.txt

frappe.ui.form.on('Question', {
	// refresh: function(frm) {
	subject: function (frm) {
		console.log(frm.doc.subject);
		//
		frm.set_query("doctor_name", "doctor_name", function () {
			return {
				"filters": {
					"subject": frm.doc.subject
				}
			};
		});

	},

});
