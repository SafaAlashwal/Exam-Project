document.querySelector("#Send").addEventListener('click', (e) => {
    const options = document.querySelectorAll('.options');
    let output = "";

    options.forEach((option, index) => {
        const selectedOption = option.querySelector('input[type="radio"]:checked');
        if (selectedOption) {
            const selectedContent = option.querySelector(`label[for="${selectedOption.id}"]`).textContent.trim();
            output += `Question ${index + 1}: ${selectedContent}\n`;
        }
    });
    output.department
    console.log(output);

    frappe.call({
        method: 'save_selected_value',

        callback: function (response) {
            console.log(response);
        }
    });
    // استيراد مكتبة الـ HTTP
    // const axios = require('axios');

    // // تعريف النقطة النهائية (endpoint) المطلوبة
    // const endpoint = '/api/resource/Resualt';

    // // البيانات المطلوب إرسالها
    // const data = {
    //     resualt: selectedContent,

    // };

    // // تنفيذ طلب POST لإضافة موظف جديد
    // axios.post(endpoint, data)
    //     .then(response => {
    //         // معالجة الاستجابة
    //         console.log(response.data);
    //     })
    //     .catch(error => {
    //         // معالجة الخطأ
    //         console.error(error);
    //     });

});