import styled from "styled-components";
import "./App.css";
import { useState } from "react";
import {
  CircleLoader,
  ClipLoader,
  DotLoader,
  SyncLoader,
} from "react-spinners";
import axios from "axios";

const Box = styled.div`
  background-color: #e9e6ff;
  max-width: 1024px;
  margin: 16px auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
`;

const Input = styled.div`
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 20px;
  border-bottom: 1px solid #ccc;
  padding: 8px;
  margin-bottom: 16px;
  select,
  button,
  input {
    padding: 8px;
    font-size: 16px;
    cursor: pointer;
  }

  img {
    width: 400px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
`;

const BASE_URL = "http://10.0.0.4:2727";

const FILTERS = {
  "Ecualización de Histograma": [],
  "Transformada Discreta de Fourier en Dos Dimensiones": [],
  "Módulo de la Transformada Discreta de Fourier en Dos Dimensiones": [],
  "Filtro Paso Bajo Ideal": ["D0"],
  "Filtro Paso Alto Ideal": ["D0"],
  "Filtro Paso Bajo Gaussiano": ["sigma"],
  "Filtro Paso Alto Gaussiano": ["sigma"],
  "Filtro Paso Bajo Butterworth": ["D0", "n"],
  "Filtro Paso Alto Butterworth": ["D0", "n"],
};

function App() {
  const [filter, setFilter] = useState(Object.keys(FILTERS)[0]);
  const [params, setParams] = useState([]);
  const [image, setImage] = useState(null);
  const [newImage, setNewImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const readImage = () =>
    new Promise((resolve, reject) => {
      var reader = new FileReader();
      reader.readAsDataURL(image);
      reader.onload = async () => {
        resolve(reader.result);
      };
    });

  const upload = async () => {
    setLoading(true);
    const img = await readImage();
    const base64 = img.split(",")[1];

    let URL = "";

    switch (filter) {
      case "Ecualización de Histograma":
        URL = BASE_URL + "/histogram-equalization/";
        break;
      case "Transformada Discreta de Fourier en Dos Dimensiones":
        URL = BASE_URL + "/discrete-fourier-transform/";
        break;
      case "Módulo de la Transformada Discreta de Fourier en Dos Dimensiones":
        URL = BASE_URL + `/discrete-fourier-transform-shift/`;
        break;
      case "Filtro Paso Bajo Ideal":
        URL = BASE_URL + `/low-pass-ideal-filter/${params[0]}/`;
        break;
      case "Filtro Paso Alto Ideal":
        URL = BASE_URL + `/high-pass-ideal-filter/${params[0]}/`;
        break;
      case "Filtro Paso Bajo Gaussiano":
        URL = BASE_URL + `/low-pass-gaussian-filter/${params[0]}/`;
        break;
      case "Filtro Paso Alto Gaussiano":
        URL = BASE_URL + `/high-pass-gaussian-filter/${params[0]}/`;
        break;
      case "Filtro Paso Bajo Butterworth":
        URL =
          BASE_URL + `/low-pass-butterworth-filter/${params[0]}/${params[1]}/`;
        break;
      case "Filtro Paso Alto Butterworth":
        URL =
          BASE_URL + `/high-pass-butterworth-filter/${params[0]}/${params[1]}/`;
        break;
      default:
        break;
    }
    const response = await axios.post(URL, {
      image: base64,
    });

    setNewImage("data:image/png;base64," + response.data.image);

    setLoading(false);
  };

  const edit = (i, v) => {
    const newParams = [...params];
    newParams[i] = v;
    setParams(newParams);
  };

  return (
    <div className="App">
      <Box>
        <h1>Filtro de imágenes online</h1>
        <div>
          <Input>
            <p>1. Seleccione el tipo de filtrado</p>
            <select value={filter} onChange={(e) => setFilter(e.target.value)}>
              {Object.keys(FILTERS).map((k) => (
                <option>{k}</option>
              ))}
            </select>
            {filter && (
              <div>
                {FILTERS[filter].map((el, i) => (
                  <input
                    value={params[i]}
                    onChange={(e) => edit(i, e.target.value)}
                    placeholder={el}
                    type="number"
                  ></input>
                ))}
              </div>
            )}
          </Input>
          <Input>
            <p>2. Seleccione la imagen</p>
            <input
              onChange={(e) => setImage(e.target.files[0])}
              type="file"
              id="img"
              name="img"
              accept="image/*"
            />
            {image && (
              <img src={URL.createObjectURL(image)} alt="preview"></img>
            )}
          </Input>
          <Input>
            <p>3. Verifique la imagen e inicie el proceso</p>
            {!loading ? (
              <button onClick={upload}>
                Iniciar el procesamiento de la imagen
              </button>
            ) : (
              <SyncLoader />
            )}
          </Input>
          <Input>
            <p>4. Observe el resultado</p>
            {newImage && <img src={newImage} alt="preview"></img>}
            {newImage && (
              <a download="result.png" href={newImage}>
                Descargar resultado
              </a>
            )}
          </Input>
        </div>
      </Box>
    </div>
  );
}

export default App;
