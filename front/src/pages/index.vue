<template>
  <div class="relative p-4" ref="board">
    <BorderBox7 :color="['white', 'white']" :key="width">
      <div class="h-full w-full" ref="panel"></div>
      <div
        class="border border-white w-80 h-64 top-8 left-8 absolute p-4 flex-y-start"
      >

        <n-upload
          :headers="{
            'naive-info': 'hello!',
          }"
          :data="{
            'naive-data': 'cool! naive!',
          }"
          class="flex-col justify-center items-center h-16"
        >
          <DvButton
            border="Border5"
            class="text-center h-10 font-semibold pt-1 w-72"
            fontSize="18px"
            fontColor="#ffffff"
          >
            上传成绩表
          </DvButton>
        </n-upload>
 
          <DvButton
            @click=mymod()
            border="Border5"
            class="text-center h-10 font-semibold pt-1 w-72"
            fontSize="18px"
            fontColor="#ffffff"
          >
            使用自定义模板
          </DvButton>




      </div>
      <div
        class="border border-white w-80 h-40 top-800 left-80 absolute p-4"
        v-if="isShow"
      >

        
        <textarea v-model="textInput" class="w-full h-40 p-2 custom-input custom-textarea" rows="20" cols="30"></textarea>
        

        
        
      </div>
            <div
        class="border border-white w-80 h-40 bottom-40 left-8 absolute p-4"
        v-if="isShow"
      >
        <textarea
          v-model="ttext"
          class="w-full p-2 custom-input custom-textarea1"
        ></textarea>
        <button @click=mysend() class="mt-4 px-4 py-2 bg-blue-500 text-white rounded-md">开始发送</button>
      </div>
    </BorderBox7>
  </div>
</template>

<script setup>
import axios from 'axios';
import { Network } from "vis-network";
import { nextTick, onMounted, ref, watch, reactive } from "vue";
import { useRouter } from "vue-router";
import switchImageUrl from "../assets/Switch.png";
import clientImageUrl from "../assets/Laptop1.png";
import switchImageUrl2 from "../assets/Server.png";
import { BorderBox7 } from "@kjgl77/datav-vue3";
import { Button as DvButton } from "@kjgl77/datav-vue3";
import { useElementSize } from "@vueuse/core";
import { useGlobalState } from "@/store";
import { NUpload, NSwitch, NButton } from "naive-ui";
import { before } from "lodash-es";
const board = ref();
const { width } = useElementSize(board);
const panel = ref();
const { isEase } = useGlobalState();
const isServer = ref(false);
const isWorker = ref(false);
const isLearning = ref(true);
const scrollingText = ref(''); // 初始化滚动文本内容
const ttext = ref('');

function mysend () {
  axios.get('http://127.0.0.1:5000/send')
  .then(response => {
    this.ttext = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
function mymod () {
  this.ttext = "modify send ok";
  axios.get('http://127.0.0.1:5000/modify', {params: {  
       text: this.textInput,
    }
  })
  .then(response => {
    this.ttext = response.data;
  })
  .catch(error => {
    console.error('Error:', error);
  });
}
const startScroll = () => {
  
  // 在点击开始发送按钮时，显示滚动文本框
    // 获取文本框的内容
  const textToScroll = "张三发送成功！\n李四发送成功！\n王五发送成功！";
  
  // 如果文本框的内容不为空，可以执行滚动
  if (textToScroll) {
    // 获取文本框元素
    const textareaElement = document.querySelector(".custom-textarea");

    // 获取滚动文本框元素
    const scrollingTextarea = document.querySelector(".custom-textarea1");

    // 将文本框的内容赋值给滚动文本框
    scrollingTextarea.value = textToScroll;

    // 添加CSS类以显示滚动文本框
    scrollingTextarea.classList.add("show");

    // 使用JavaScript或其他库来实现滚动效果
    // 这里可以添加你选择的滚动实现逻辑
  }
  axios.get('http://127.0.0.1:5000/send');
  // 在这里可以触发滚动动画效果，滚动显示文本内容
  // 你可以使用 CSS 动画或 JavaScript 动画库来实现滚动效果
};
const textInput = ref("亲爱的XXX同学:\n你的成绩单为\nXXX\n继续加油\n"); // 初始化文本框的数据
const options = {
  nodes: {
    font: {
      color: "#fff",
    },
    color: "#fff",
  },
  edges: {
    color: "rgba(255,255,255,0.2)",
  },
  layout: {
    hierarchical: {
      direction: "LR",
    },
  },
};
const nodes = [
  {
    id: 1,
    label: "pc1",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 2,
    label: "pc2",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 3,
    label: "pc3",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 4,
    label: "pc4",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 5,
    label: "pc5",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 6,
    label: "pc6",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 7,
    label: "pc7",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 8,
    label: "pc8",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 9,
    label: "pc9",
    level: 1,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 10,
    label: "S1",
    level: 5,
    image: switchImageUrl,
    shape: "image",
  },
  {
    id: 11,
    label: "S2",
    level: 5,
    image: switchImageUrl,
    shape: "image",
  },
  {
    id: 12,
    label: "S3",
    level: 3,
    image: switchImageUrl,
    shape: "image",
  },
  {
    id: 13,
    label: "S4",
    level: 6,
    image: switchImageUrl,
    shape: "image",
  },
  {
    id: 14,
    label: "S5",
    level: 4,
    image: clientImageUrl,
    shape: "image",
  },
  {
    id: 15,
    label: "S6",
    level: 4,
    image: clientImageUrl,
    shape: "image",
  },
];
function createDot(hexColor) {
  return {
    enabled: true,
    type: "image",
    imageWidth: 12,
    imageHeight: 12,
    src: `data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' style='width:24px;height:24px' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='12' r='10' fill='%23${hexColor.slice(
      1
    )}' /%3E%3C/svg%3E`,
  };
}
const redDot = createDot("#ff0000");
const greenDot = createDot("#00ff00");
const yellowDot = createDot("#EAB308");
const edges = [
  {
    from: 1,
    to: 10,
    // arrows: {
    //   to: greenDot,
    //   from: greenDot,
    // },
  },
  {
    from: 2,
    to: 10,
    // arrows: {
    //   to: isEase.value ? yellowDot : redDot,
    //   from: isEase.value ? yellowDot : redDot,
    // },
  },
  {
    from: 3,
    to: 10,
    // arrows: {
    //   to: greenDot,
    //   from: greenDot,
    // },
  },
  {
    from: 4,
    to: 10,
    // arrows: {
    //   to: isEase.value ? yellowDot : redDot,
    //   from: isEase.value ? yellowDot : redDot,
    // },
  },
  {
    from: 4,
    to: 11,
    // arrows: {
    //   to: isEase.value ? yellowDot : redDot,
    //   from: isEase.value ? yellowDot : redDot,
    // },
  },
  {
    from: 5,
    to: 12,
    // arrows: {
    //   to: isEase.value ? greenDot : redDot,
    //   from: isEase.value ? greenDot : redDot,
    // },
  },
  {
    from: 6,
    to: 12,
    // arrows: {
    //   to: isEase.value ? greenDot : redDot,
    //   from: isEase.value ? greenDot : redDot,
    // },
  },
  {
    from: 7,
    to: 14,
    // arrows: {
    //   to: greenDot,
    //   from: greenDot,
    // },
  },
  {
    from: 8,
    to: 14,
  },
  {
    from: 9,
    to: 15,
  },
  {
    from: 11,
    to: 12,
  },
  {
    from: 11,
    to: 13,
  },
  {
    from: 11,
    to: 14,
  },
  {
    from: 13,
    to: 15,
  },
  {
    from: 14,
    to: 15,
  },
];
const router = useRouter();
function renderNets() {
  // console.log(isServer.value);
  if (isServer.value) {
    nodes[9] = {
      id: 10,
      label: "S1",
      level: 5,
      image: switchImageUrl2,
      shape: "image",
    };
  } else {
    nodes[9] = {
      id: 10,
      label: "S1",
      level: 5,
      image: switchImageUrl,
      shape: "image",
    };
  }
  function startScroll1(){
    axios.post('http://127.0.0.1:5000/modify', {text: textInput.value})
    .then(response => {
      networkData.flowtable_text = response.data;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }
  console.log(nodes[9]);
  new Network(panel.value, { nodes, edges }, options).on(
    "doubleClick",
    function (params) {
      const label = nodes.find((v) => v.id === params.nodes[0]).label;
      if (label.startsWith("S")) router.push(`/flow?label=${label}`);
      // alert(JSON.stringify(params, null, 4))
    }
  );
}
const networkData = reactive({
  train_loss: "",
  train_acc: "",
  val_loss: "",
  val_acc: "",
});
onMounted(() => {

});

watch(width, () => {

});

watch(isEase, () => {
  if (isEase.value) {
    nextTick(() => {
      setTimeout(() => {
        changeShow2();
        isLearning.value = false;
      }, 5000);
    });
  } else {
    isLearning.value = true;
    networkData.train_loss = "";
    networkData.train_acc = "";
    networkData.val_loss = "";
    networkData.val_acc = "";
  }
});
watch(isLearning, () => {
  if (!isLearning.value) {
    nextTick(() => {
      if (isShow.value) {
        changeShow2();
      } else {
        changeShow1();
      }
    });
  }
});
watch(isServer, () => {
  nextTick(() => {

  });
});
watch(isWorker, () => {
  nextTick(() => {
    // 改变主机图片
  });
});

const isShow = ref(true);
function changeShow1() {
  isShow.value = false;
  if (!isLearning.value) {
    networkData.train_loss = "0.234";
    networkData.train_acc = "0.989";
    networkData.val_loss = "0.012";
    networkData.val_acc = "0.956";
  }
}
function changeShow2() {
  isShow.value = true;
  if (!isLearning.value) {
    networkData.train_loss = "0.012";
    networkData.train_acc = "0.978";
    networkData.val_loss = "0.234";
    networkData.val_acc = "0.967";
  }
}
const dataFileList = reactive([]);
const codeFileList = reactive([]);

// 文件上传和删除
const beforeUploadData = () => {
  console.log("before upload data");
  return true;
};
const beforeUploadCode = () => {
  console.log("before upload code");
  return true;
};
// const uploadData = (item) => {
//   console.log("item" + item.file);
//   dataFileList.push(item.file);
// };
const uploadFiles = () => {
  // 遍历文件列表，处理每个文件的上传逻辑
  dataFileList.forEach((file) => {
    const reader = new FileReader();

    reader.onload = (event) => {
      // 文件读取成功后的处理逻辑
      const fileData = event.target.result;
      console.log(fileData);
    };

    reader.onerror = (event) => {
      // 文件读取失败的处理逻辑
      console.error("文件读取失败");
    };

    reader.readAsDataURL(file); // 以DataURL的形式读取文件内容
  });
};
const uploadData = ({ file }) => {
  console.log("upload data");
  dataFileList.push(file.file);
};
const uploadCode = (item) => {
  console.log(item);
  codeFileList.push(item.file);
};
const finishData = () => {
  console.log("上传成功data");
};
const finishCode = () => {
  console.log("上传成功code");
};
</script>
<style scoped>
.custom-input {
  color: black !important; /* 设置字体颜色为蓝色，你可以根据需要更改颜色值 */
  /* 可以添加其他自定义样式，例如字体大小、背景颜色等 */
}
.custom-textarea {
  width: 700px; /* 设置宽度 */
  height: 600px; /* 设置高度 */
  /* 可以根据需要调整宽度和高度 */
  position: absolute; /* 设置位置属性为绝对定位 */
  top: -650px; /* 设置距离顶部的位置 */
  left: 200px; /* 设置距离左侧的位置 */
  background: rgba(255, 255, 255, 0.518)
}
.custom-textarea1 {
  width: 230px; /* 设置宽度 */
  height: 50px; /* 设置高度 */
  /* 可以根据需要调整宽度和高度 */
  position: absolute; /* 设置位置属性为绝对定位 */
  top: 120px; /* 设置距离顶部的位置 */
  left: 20px; /* 设置距离左侧的位置 */
}
.bottom-4 {
  
  bottom: 4px;
  transition: bottom 0.5s; /* 添加过渡效果 */
}

.bottom-4.show {
  bottom: 20px; /* 滚动后的位置，你可以根据需要调整 */
}
.flex-y-start {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>

