<template>
    <h1>Jobs</h1>
    <div v-if="jobs.length">
        <div v-for="job, idx in jobs" :key="idx" class="job">
            <router-link :to="{ name: 'job_details', params: { id: job.id } }">
                <h2>{{ job.title }}</h2>
            </router-link>
        </div>
    </div>
    <div v-else-if="err_mssg">
        <p>{{ err_mssg }}</p>
    </div>
    <div v-else>
        <p>Loading Jobs...</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            // jobs: [
            //     { title: "Ninja UX Designer", id: 1, details: "Ux designer Detailed" },
            //     { title: "Ninja Web Developer", id: 2, details: "website Developer Detailed" },
            //     { title: "Ninja Vue Developer", id: 3, details: "vue Developer Detailed" },
            // ]
            jobs: [],
            err_mssg: null,
        }
    },

    mounted() {
        fetch("http://localhost:3000/jobs")
            .then((res) => res.json())
            .then((data) => this.jobs = data)
            .catch(err => {
                        console.log(err.message); this.err_mssg = err.message
                    } 
                )
    }
}

</script>

<style>
.job h2 {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
    margin: 10px auto;
    max-width: 600px;
    cursor: pointer;
    color: #444;
}

.job h2:hover {
    background: #ddd;
}

.job a {
    text-decoration: none;
}
</style>