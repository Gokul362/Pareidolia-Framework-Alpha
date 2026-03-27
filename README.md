# Pareidolia-Framework-Alpha
Pareidolia Framework (Alpha Version)

Lead Architect: [Gokul]

Tech Stack: Python (System Logic) | C# (Implementation Research) | YAML (Data Schema)

 Project Overview
Pareidolia is a data-driven framework designed to bridge the gap between engine architecture and creative content. The goal is to eliminate "clunker" development cycles by allowing real-time, non-destructive logic injection into active game states.

This repository serves as the Alpha Prototype for the core systems that will power the Cost of Legends platform.

Key Systems:

Hot Reloader: Script that monitors any changes within a file, and if a change is detected, the values will update almost instantly

YAML-Driven Architecture: All game variables shall be in human readable YAML files, to ensure that level designers can tweak values without touching any core code

Binary Injection Pipeline: Those human readable YAML files shall be compiled and compressed into optimized ".pxb" (Pareidolia Binary) files 

Licensing info:
This prototype is licensed under the MIT License. The underlying game IP (Cost of Legends) and future C++ implementations remain proprietary.
