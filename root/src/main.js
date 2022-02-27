import './styles/style.css'
import * as THREE from 'three'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { MTLLoader } from 'three/examples/jsm/loaders/MTLLoader';
import * as dat from 'dat.gui'
import { ambientLight, pointLight } from './components/lights';
import { gCube, gPlane } from './components/geometry';
import  MouseMeshInteraction  from './components/mmi';
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
const mmi = new MouseMeshInteraction(scene, camera);
// Materials //
const basicTestMat = new THREE.MeshStandardMaterial()
basicTestMat.color = new THREE.Color(0xFFE102)
const basicTestMat2 = new THREE.MeshStandardMaterial()
basicTestMat2.color = new THREE.Color(0x0012FF)
const basicTestMat3 = new THREE.MeshNormalMaterial({ wireframe: true })


// Objects //
const testPlane = new THREE.Mesh(gPlane, basicTestMat)
testPlane.rotation.set(-1.5, 0, 0)
testPlane.position.set(0, -3, 0)
scene.add(testPlane)

let arrCubes = [];
for(var i=0; i < 9 ;i++){
    const cubeTest = new THREE.Mesh(gCube, basicTestMat2)
    if(i < 1){
        cubeTest.position.set(0 , 0, 0)
    }else if(i == 1){
    cubeTest.position.set(1.1 , 0, 0)
    }else if(i == 2){
    cubeTest.position.set(1.1 , -1.1, 0)
    }else if(i == 3){
    cubeTest.position.set(0 , -1.1, 0)
    }else if(i == 4){
    cubeTest.position.set(-1.1 , -1.1, 0)
    }else if(i==5){
    cubeTest.position.set(-1.1 , 0, 0)
    }else if(i==6){
    cubeTest.position.set(-1.1 , 1.1, 0)
    }else if(i==7){
    cubeTest.position.set(0 , 1.1, 0)
    }else if(i==8){
    cubeTest.position.set(1.1 , 1.1, 0)
    }
    arrCubes.push(cubeTest);
    arrCubes[i].name = 'cubeFront';
    scene.add(arrCubes[i]);
    
}

mmi.addHandler('cubeFront', 'click', () => {
    console.log("ciaosd");
    
})

// const cubeTest = new THREE.Mesh(gCube,basicTestMat2)
// cubeTest.position.set(0,.9,0)
// scene.add(cubeTest)


// Lights //
scene.add(ambientLight)
pointLight.position.set(0, 10, 10)
scene.add(pointLight)


// Update //
let j = 1;
let radians = 0;
const clock = new THREE.Clock()
const tick = () => {
    if(j > 8){
        j = 1;
    }
    radians += 1

    arrCubes[j].position.x = arrCubes[j].position.x + Math.cos(radians) 
    arrCubes[j].position.y = arrCubes[j].position.y + Math.sin(radians) 

    // pointLight.position.x = Math.cos(radians)
    // pointLight.position.y = Math.sin(radians)
    mmi.update();
     controls.update()
    renderer.render(scene, camera)
    window.requestAnimationFrame(tick)
    j++;
}

tick();