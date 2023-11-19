
const ctx = document.getElementById('fstChart');


new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1,
      fill: false,
      borderColor: 'red',
      tension: 0.1
    }]
  },
  // options: {
  //   scales: {
  //     y: {
  //       beginAtZero: true
  //     }
  //   }
  // }

});


