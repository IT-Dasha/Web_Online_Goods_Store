 let qwe = document.getElementById('categoryName').value; // "123"
        // Данные для диаграммы — подставьте реальные данные или используйте заглушки
        // Если хотите, чтобы данные передавались из Django, нужно изменить view и передать контекст
        const categories = [
            "Основной товар",
            "LabArte Техномассив Royal Parket"
            // добавьте другие категории, если нужно
        ];

        const values = [
            qwe,  // например, количество характеристик для "Основной товар"
            1   // для "LabArte Техномассив Royal Parket"
        ];

        const ctx = document.getElementById('categoryChart').getContext('2d');
        const categoryChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: categories,
                datasets: [{
                    label: 'Количество характеристик',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        precision: 0
                    }
                }
            }
        });