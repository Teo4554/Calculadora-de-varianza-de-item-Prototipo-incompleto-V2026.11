# Cronbach's Alpha Calculator (Prototype Version) 📊

Este repositorio contiene la versión prototipo de un script en Python diseñado para ayudar en la fase inicial del cálculo de la consistencia interna mediante el **Alfa de Cronbach** en pruebas o cuestionarios.

## 📝 Descripción

En su estado actual, este prototipo permite recopilar información general sobre la prueba (número de ítems y tamaño de la muestra) y calcula la **varianza muestral de las puntuaciones totales de un ítem individual**, procesando las diferencias con respecto al promedio y elevándolas al cuadrado.

> **Nota:** Esta es una versión preliminar/prototipo enfocada en la lógica básica del procesamiento de datos por ítem. Próximamente se subirá la versión completa que automatizará el cálculo global del Alfa de Cronbach para múltiples ítems.

---

## 🚀 Características del Prototipo

* Requisición interactiva de parámetros iniciales ($K$ ítems, $N$ participantes).
* Cálculo iterativo del promedio de puntajes.
* Desviación individual de cada puntaje respecto a la media ($X_i - \bar{X}$).
* Cálculo de varianza muestral empleando la fórmula:
  $$s^2 = \frac{\sum (X_i - \bar{X})^2}{N - 1}$$

---

## 🛠️ Requisitos e Instalación

No se requieren librerías externas. Solo necesitas tener instalado **Python 3.x**.

1. Clona este repositorio:
   ```bash
   git clone https://github.com/teo4554/Calculadora-de-varianza-de-item-Prototipo-incompleto-V2026.11.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Calculadora-de-varianza-de-item-Prototipo-imcompleto-V2026.11
   ```

---

## 💻 Uso

Ejecuta el script desde tu terminal:

```bash
python Cronbach.py
```

Sigue las instrucciones en pantalla para ingresar el número de ítems, el número de participantes y sus respectivos puntajes.

---

## 📌 Próximos Pasos (Versión Completa)

- [ ] Soporte para matrices de datos completas (múltiples ítems por participante).
- [ ] Cálculo automático de la suma de las varianzas de los ítems ($\sum s_i^2$).
- [ ] Cálculo de la varianza total ($s_T^2$).
- [ ] Obtención directa del coeficiente Alfa de Cronbach ($\alpha$).
- [ ] Carga de datos mediante archivos `.csv` o `.xlsx`.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
