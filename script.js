document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const file = document.getElementById("fileInput").files[0];
    const template = document.getElementById("template").value;
    const formData = new FormData();
    formData.append("file", file);
    formData.append("template", template);
  
    const res = await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });
  
    const data = await res.json();
    document.getElementById("result").innerHTML =
      "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
  });
  