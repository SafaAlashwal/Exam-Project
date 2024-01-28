frappe.pages['page-question-1'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Page Question',
		single_column: true
	});
}