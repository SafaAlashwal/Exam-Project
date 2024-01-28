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
    fetch('http://localhost:8004/api/save_selected_value', { // استبدل بعنوان الخادم الصحيح
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            selected_value: output
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    console.log(output);
});