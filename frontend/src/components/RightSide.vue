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
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, autem
      quis. Animi sunt labore id veniam tempora adipisci aspernatur quam facere
      sequi eos totam, iusto praesentium voluptates. Mollitia, consectetur
      reprehenderit! Libero pariatur cum temporibus magnam, commodi itaque iste
      esse necessitatibus repellendus obcaecati maxime et totam eveniet
      praesentium vitae facilis dolores!
    </p>
  </div>
</template>
