function togglePassword() {
    var passwordField = document.getElementById("password");
    if (passwordField.type === "password") {
        passwordField.type = "text";
    } else {
        passwordField.type = "password";
    }
}

let scene, camera, renderer, particles;

function initThreeJS() {
    // Create the Three.js scene
    scene = new THREE.Scene();
    scene.background = null; // Keep background transparent

    // Set up the camera
    let container = document.querySelector(".ambience");
    let width = container.clientWidth;
    let height = container.clientHeight;
    camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    camera.position.z = 3;

    // WebGL Renderer with transparent background
    renderer = new THREE.WebGLRenderer({ alpha: true });
    renderer.setSize(width, height);
    container.appendChild(renderer.domElement);

    // Particle setup
    const particleGeometry = new THREE.BufferGeometry();
    const particleCount = 1000;
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i += 3) {
        let phi = Math.acos(2 * Math.random() - 1);
        let theta = Math.random() * Math.PI * 2;
        let r = 1.5;

        positions[i] = r * Math.sin(phi) * Math.cos(theta);
        positions[i + 1] = r * Math.sin(phi) * Math.sin(theta);
        positions[i + 2] = r * Math.cos(phi);
    }

    particleGeometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    const particleMaterial = new THREE.PointsMaterial({ color: "#8A2BE2", size: 0.02 }); // Neon Purple
    particles = new THREE.Points(particleGeometry, particleMaterial);
    scene.add(particles);

    animate();
}

function animate() {
    requestAnimationFrame(animate);
    particles.rotation.y += 0.002;
    renderer.render(scene, camera);
}

// Handle window resizing
window.addEventListener("resize", () => {
    let container = document.querySelector(".ambience");
    let newWidth = container.clientWidth;
    let newHeight = container.clientHeight;
    renderer.setSize(newWidth, newHeight);
    camera.aspect = newWidth / newHeight;
    camera.updateProjectionMatrix();
});




// Initialize Three.js when the page loads
window.onload = function () {
    initThreeJS();
    $('#nameID').change(function(){
        console.log('triggereD')
        $('.annon-login')
            .prop('disabled', false)
            .css('background-color', 'green')
    })
    
};
