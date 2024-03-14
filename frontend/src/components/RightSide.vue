<template>
  <div class="container border border-2 rounded-4 shadow-sm p-3 mb-5">
    <nav class="navbar bg">
      <div class="container-fluid">
        <form class="d-flex" role="search">
          <input
            class="form-control me-2"
            type="search"
            placeholder="Search"
            aria-label="Search"
          />
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </nav>
    <label for="customRange2" class="form-label mb-0"
      ><p class="fs-6 fw-light mb-0">ratio of text to comment</p></label
    >
    <input type="range" class="form-range" min="0" max="5" id="customRange2" />
    <div class="container">
      <strong>Summary</strong>

      <p class="text-center fs-6 fw-light">
        <span class="text-decoration-underline text-info-emphasis"
          >Content Part:
        </span>
        {{ msgDict["content"] }}
        <span class="text-decoration-underline fw-light text-info-emphasis"
          >Comments Part:
        </span>
        {{ msgDict["comment"] }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RightSide",
  data() {
    return {
      // 接受字典数据
      msgDict: {
        state: "",
        summary: "",
        content: "",
        comment: "",
      },
    };
  },
  methods: {
    getResponse() {
      const path = "http://127.0.0.1:5000/";
      axios
        .get(path)
        .then((res) => {
          this.msgDict = res.data;
          console.log(res.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.getResponse();
  },
};
</script>
