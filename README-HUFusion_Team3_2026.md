# HUFusion_Team3_2026

![GitHub Repository Owner](https://img.shields.io/badge/Owner-patrickmicahjanes--beep-blue)
![GitHub Stars](https://img.shields.io/github/stars/patrickmicahjanes-beep/HUFusion_Team3_2026?style=flat-square)
![GitHub Forks](https://img.shields.io/github/forks/patrickmicahjanes-beep/HUFusion_Team3_2026?style=flat-square)
![License](https://img.shields.io/badge/License-Unspecified-lightgrey)

This repository serves as the central hub for the hall probe team involved in Hampton University's STAR_Lite project. 

---

## 📖 Table of Contents

1.  [Key Features & Benefits](#key-features--benefits)
2.  [Project Structure](#project-structure)
3.  [Prerequisites & Dependencies](#prerequisites--dependencies)
4.  [Contributing and Installation Guidelines](#installation--setup-instructions)
5.  [License Information](#license-information)
6. [Acknowledgments](#acknowledgments)
3.  [Prerequisites & Dependencies](#prerequisites--dependencies)
4.  [Contributing and Installation Guidelines](#installation--setup-instructions)
5.  [License Information](#license-information)
6. [Acknowledgments](#acknowledgments)

---

## 🌟 Key Features & Benefits

This repository is designed to be a living knowledge base for the HUFusion hall probe team, offering the following:

*   **Centralized Documentation:** A single source for all information regarding magnetic field systems, probing devices, data acquisition, and software solutions..
*   **Collaboration Hub:** Facilitates collaboration among permitted individuals by providing a platform for sharing insights, updates, and best practices.

---

## 📂 Project Structure


###The repository is organized as follows:
**`Complete Guide To Magnetic Field Systems.md`**: This is an auxiliary document to understand the STAR_Lite magnetic field measurement strategy in the context of that of the fusion industry as a whole. Other information such as accurate magnetic field measurement practices and the significance of LTS systems in field measurement studies are also outlined there.


###Auxilliary files and resources:
Most of the code required for the project is organized in this repository. Any pdf's or other files that are not code are linked to below.

An overview of the hardware needed for this project is provided in the slideshow linked below
https://docs.google.com/presentation/d/1VGAAb63L0qQeKwDfRUkr5AzK5K9MUun-I3ZwrXb01p8/edit?slide=id.p#slide=id.p

The following is a link to the Overleaf document that contains the more technical details of the project updated to the most recent edits. PDF versions of the document can be downloaded from the Overleaf link as well.
https://www.overleaf.com/read/fbgqqshqdvhg#07850f


####Important manuals: 

Hall probes: 
This link includes the most recent documentation: https://senisens.com/sensors/3dhall-3-axis-hall-magnetic-sensor-senm3dx/#downloads
However, old versions, particularly v2.0, reveal some of the more technical details of the hall probe that are not included in the most recent documentation. It is however, recommended to confirm that any information found in the older versions is still relevant to the current hardware. Other versions can usually be found by searching for "senis senm3dx manual X.X" on the web, where X.X is the version number. It may be that each version increases in version number by 0.1, but so far, the following versions have been found online: 1.2, 2.0, 2.4, and 2.5.


DAQ Boards: 
Pdf's for the DAQ boards used in this project can be found at the following links:  
Due to confidentiality concerns mentioned in the document, preliminary product information from OCTO-BEE-CELF_Design-1.pdf will not be shared on this repository. However, the pdf is accessible on the 3DHall user of Dr. C. Lowe's computer to anyone who has been permitted to view it.

LTS System: 
https://www.manualslib.com/products/Thorlabs-Lts300-12183865.html

## 🛠️ Prerequisites & Dependencies

*   **Markdown Viewer/Editor:** Any text editor or IDE with Markdown preview capabilities (e.g., VS Code, Typora, GitHub's web interface) to comfortably read or contribute to the documentation.

For users with access to the associated hardware, the following are needed: 
* Access to Gitbash or any Git client (to run HAPI) and access to Phoebus via the ACQ400CSSP file. Both of these have historically been available on Dr. C. Lowe's computer on the user 3DHall.

For users with access to the associated hardware, the following are needed: 
* Access to Gitbash or any Git client (to run HAPI) and access to Phoebus via the ACQ400CSSP file. Both of these have historically been available on Dr. C. Lowe's computer on the user 3DHall.




## 👋 Contributing and Installation Guidelines


To contribute:

1.  **Fork the Repository:** Click the 'Fork' button at the top right of this repository page on GitHub.
2.  **Clone Your Fork:** Clone your forked repository to your local machine.
    ```bash
    git clone https://github.YOUR_GITHUB_USERNAME/HUFusion_Team3_2026.git
    cd HUFusion_Team3_2026
    ```
3.  **Create a New Branch:** Create a dedicated branch for your changes.
    ```bash
    git checkout -b feature/your-feature-name-or-docs-update
    ```
4.  **Make Your Changes:**
    *   Update `Complete Guide To Magnetic Field Systems.md` with new information, corrections, or expanded explanations.
    *   Ensure any new sections or significant changes are reflected in the document's Table of Contents.
    *   Maintain clarity, conciseness, and adhere to Markdown formatting best practices.
5.  **Commit Your Changes:**
    ```bash
    git add .
    git commit -m "feat: Add detailed section on [topic] to guide"
    ```
6.  **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature-name-or-docs-update
    ```
7.  **Create a Pull Request (PR):**
    *   Go to your forked repository on GitHub and click the "Compare & pull request" button.
    *   Provide a clear title and description for your PR, explaining the changes you've made.
    *   Request a review from relevant team members.



If you do not have permissions to contribute to this repository and want to be able to edit it, simply clone it to your machine:
If you do not have permissions to contribute to this repository and want to be able to edit it, simply clone it to your machine:

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** where you want to store the repository.
3.  **Execute the following command:**
    ```bash
    git clone https://github.com/patrickmicahjanes-beep/HUFusion_Team3_2026.git
    ```
4.  **Change into the repository directory:**
    ```bash
    cd HUFusion_Team3_2026
    ```

## ⚖️ License Information

This project currently has **no specified license**. This means that by default, all rights are reserved by the copyright holder(s) (i.e., patrickmicahjanes-beep and Hampton University).

---

## 🙏 Acknowledgments

We extend our gratitude to:

*   **Hampton University:** For initiating and supporting the STAR_Lite project.
*   **The STAR_Lite Project Team:** For their collaborative efforts and dedication.