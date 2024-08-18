document.getElementById("uploadBtn").addEventListener("click", function () {
  const fileInput = document.getElementById("logfile");
  const file = fileInput.files[0];

  if (file) {
    const formData = new FormData();
    formData.append("file", file);

    // Send the file to the Flask API using fetch
    fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert("Error: " + data.error);
        } else {
          alert("Success: " + data.message);
          console.log("File uploaded successfully, file path:", data.file_path);
          localStorage.setItem("uploadedFilePath", data.file_path);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("File upload failed!");
      });
  } else {
    alert("Please select a file to upload.");
  }
});

document.getElementById("logfile").addEventListener("change", function () {
  const fileName = this.value.split("\\").pop();
  this.nextElementSibling.innerHTML = fileName;
});


document.getElementById("generateBtn").addEventListener("click", function () {
  const filePath = localStorage.getItem("uploadedFilePath");

  if (filePath) {
    const requestData = {
      file_path: filePath,
    };

    // Send the file path to the Flask API for analysis
    fetch("http://127.0.0.1:5000/api/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert("Error: " + data.error);
        } else {
          console.log("Analysis Result:", data);
          alert("Log analysis completed successfully!");
          // You can further process the JSON response here
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Log analysis failed!");
      });
  } else {
    alert("Please upload a file first.");
  }
});