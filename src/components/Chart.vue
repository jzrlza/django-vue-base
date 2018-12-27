<template>
  <div>
    <ve-line :data="chartData"></ve-line>
  </div>
</template>

<script>
import VeLine from 'v-charts/lib/line.common'
export default {
  name: 'Chart',
  components: { VeLine },
  data () {
    return {
      chartData: {
        columns: ['date', 'Temperature (C)'],
        rows: [
          { 'date': '01-01', 'Temperature (C)': 25 },
          { 'date': '01-02', 'Temperature (C)': 10 },
          { 'date': '01-03', 'Temperature (C)': -8 },
          { 'date': '01-04', 'Temperature (C)': 18 },
          { 'date': '01-05', 'Temperature (C)': 30 },
          { 'date': '01-06', 'Temperature (C)': 5 },
        ]
      }
    }
  }
}
</script>