<template>
    <div class="flex flex-row w-full h-screen text-neutral-600">
        <div class="w-60 h-screen bg-stone-100">
            <h1 class="text-base pl-4 py-4 font-semibold">通知一覧</h1>
            <ul>
                <li>
                    <a class="flex justify-between flex-row px-4 py-2 border-y border-stone-200" href="">
                        <div class="flex">
                            <img class="w-10 h-10 rounded-full object-cover mr-3 bg-white" src="../../public/images/girl.png">
                            <div>
                                <h1 class="font-semibold">ユーザーA</h1>
                                <h2 class="text-xs font-light text-neutral-500">友達申請が届いています</h2>
                            </div>
                        </div>
                        <div class="flex items-center ">
                            <font-awesome-icon icon="fa-solid fa-circle-exclamation" />
                        </div>
                    </a>
                </li>
            </ul>
        </div>
        <div class="flex items-center justify-center w-6 h-20 mt-40 bg-stone-100 rounded-tr-lg rounded-br-lg">
            <font-awesome-icon icon="fa-solid fa-bell" />
        </div>
    </div>
</template>
<script>
export default {
  name:"notice-modal"
}
</script>