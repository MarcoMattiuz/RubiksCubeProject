import './styles/style.css'
import * as THREE from 'three'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { MTLLoader } from 'three/examples/jsm/loaders/MTLLoader';
import * as dat from 'dat.gui'
import { ambientLight, pointLight } from './components/lights';
import { gCube, gPlane } from './components/geometry';

// Canvas //
const canvas = document.querySelector('#bg')
const sizes = {
    width: window.innerWidth,
    height: window.innerHeight
}
window.addEventListener('resize', () => {
    sizes.width = window.innerWidth
    sizes.height = window.innerHeight
    camera.aspect = sizes.width / sizes.height
    camera.updateProjectionMatrix()
    renderer.setSize(sizes.width, sizes.height)
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
})


// Scene //
const scene = new THREE.Scene()

// Camera //
const camera = new THREE.PerspectiveCamera(75, sizes.width / sizes.height, 0.1, 100)
camera.position.set(0, 0, 10)
scene.add(camera)
// Renderer //
const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true
})
renderer.setSize(sizes.width, sizes.height)
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
// Controls
const controls = new OrbitControls(camera, canvas)
controls.enableDamping = true

// Materials //
const basicTestMat = new THREE.MeshStandardMaterial()
basicTestMat.color = new THREE.Color(0xFFE102)
const basicTestMat2 = new THREE.MeshStandardMaterial()
basicTestMat2.color = new THREE.Color(0x0012FF)

// Objects //
const testPlane = new THREE.Mesh(gPlane, basicTestMat)
testPlane.rotation.set(5, 0, 0)
scene.add(testPlane)
let arrCubes = [];
for (var i = 0; i < 5; i++) {
    const cubeTest = new THREE.Mesh(gCube, basicTestMat2)
    arrCubes.push(cubeTest)
    arrCubes[i].position.set(i * 1.5, i, 0)
    scene.add(arrCubes[i])
}
console.log(arrCubes)

// const cubeTest = new THREE.Mesh(gCube,basicTestMat2)
// cubeTest.position.set(0,.9,0)
// scene.add(cubeTest)


// Lights //
// scene.add(ambientLight)
pointLight.position.set(0, 10, 10)
scene.add(pointLight)


// Update //
let j = 0;
let radians = 0;
let x = arrCubes[1].position.x
let y = arrCubes[1].position.y
const clock = new THREE.Clock()
const tick = () => {
    if (j >= arrCubes.length) {
        j = 0;
    }

    
    // // arrCubes[j].position.x = Math.cos(radians);
    // // arrCubes[j].position.z = Math.sin(radians);
    // arrCubes[j].rotation.x = 0.7 * clock.getElapsedTime()
    // arrCubes[j].rotation.y = 0.7 * clock.getElapsedTime()
    // testPlane.rotation.z = 0.7 * clock.getElapsedTime()
    radians += 0.005
    pointLight.position.x = Math.cos(radians)
    pointLight.position.y = Math.sin(radians)

    controls.update()
    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
    j++;
}

tick();