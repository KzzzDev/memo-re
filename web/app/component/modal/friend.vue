<template>
    <div class="flex flex-row w-full h-screen text-neutral-600">
        <div class="w-60 h-screen bg-stone-200">
            <ul class="py-8">
                <li>
                    <a class="flex flex-row pl-8" href="">
                        <img class="w-12 h-12 rounded-full object-cover mr-3 bg-white" src="../../public/images/zundamon.jpg">
                        <div>
                            <h1 class="text-xl font-semibold">ずんだもん</h1>
                            <h2 class="text-sm font-light">zundamon</h2>
                        </div>
                    </a>
                </li>
            </ul>
            <h1 class="text-xs pl-2 pb-2 font-semibold">フレンドリスト</h1>
            <ul>
                <li>
                    <router-link class="flex flex-row pl-8 py-2 border-y border-neutral-300" to="/brain/2">
                        <img class="w-10 h-10 rounded-full object-cover mr-3 bg-white" src="../../public/images/girl.png">
                        <div>
                            <h1 class="font-semibold">ユーザーA</h1>
                            <h2 class="text-xs font-light">userA</h2>
                        </div>
                    </router-link>
                </li>
            </ul>
        </div>
        <div class="flex items-center justify-center w-6 h-20 mt-20 bg-stone-200 rounded-tr-lg rounded-br-lg">
            <font-awesome-icon icon="fa-solid fa-user-group" />
        </div>
    </div>
</template>

<script lang="js">
export default {
  name:"friend-modal"
}
</script>

<style scoped>

</style>