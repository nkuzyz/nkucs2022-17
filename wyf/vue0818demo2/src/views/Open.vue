<template>
    <div class="container">
        <div class="row">
            <div class="col-lg-8  offset-lg-2">
                <h3 class="mt-5">Live Streaming</h3>
                <img src="{{ url_for('http://localhost:5000/video_start') }}" width="100%">
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            imgSrc: ''
        }
    },
    mounted() {
        // axios.get('http://localhost:5000/video_start').then(res => {
        //     console.log(res);
        //     this.imgSrc = res.data
        // }).catch(err => {
        //     console.log(err);
        // });
    }
}
</script>


<style scoped>
@import url("https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css");

</style>
<!-- <template>
    <div></div>
</template>
<script>
export default {
    mounted() {
        window.location.href = 'index.html'
    }
}
</script> -->
