<script setup>

import closeSVG from '@/assets/close.svg'
import { watchEffect } from 'vue';

const props = defineProps({
  show: Boolean
})

const emit = defineEmits(['closePopup']);

watchEffect(() => {
  if (props.show) {
    document.body.classList.add('popup-open');
  } else {
    document.body.classList.remove('popup-open');
  }
})

</script>

<template>
  <Transition name="popup">
    <div v-if="show" class="popup-mask" @click.self="emit('closePopup')">
      <div class="popup-container" ref="popup">
        <div @click="emit('closePopup')" class="popup-close">
          <img :src="closeSVG" alt="close">
        </div>
        <slot></slot>
      </div>
    </div>
  </Transition>
</template>

<style>
.popup-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
  justify-content: flex-end;
  overflow-y: hidden;
}

.popup-container {
  position: relative;
  width: 30vw;
  top: 0;
  bottom: 0;
  right: 0;
  background-color: #fff;
  transition: all 0.3s ease;
}

.popup-close {
  position: absolute;
  cursor: pointer;
  top: 0.3vw;
  right: 0.3vw;
  width: 3vw;
  height: 3vw;
}

.popup-close img {
  width: 100%;
  height: 100%;
}

.popup-enter-from {
  opacity: 0;
}

.popup-leave-to {
  opacity: 0;
}

.popup-enter-from .popup-container,
.popup-leave-to .popup-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.popup-open {
  overflow-y: hidden;
}


@media (max-width: 780px) {

  .popup-container {
    width: 50vw;
  }

  .popup-close {
    width: 5vw;
    height: 5vw;
  }
}

@media (max-width: 500px) {

  .popup-container {
    width: 100%;
    background-color: #fff;
    transition: all 0.3s ease;
  }

  .popup-close {
    width: 10vw;
    height: 10vw;
  }
}
</style>