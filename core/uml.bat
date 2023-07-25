pyreverse --output puml --colorized -A --output-directory core core
python -m plantuml packages.puml
python -m plantuml classes.puml
ren classes.png core_classes_updated.png
ren packages.png core_packages_updated.png
ren classes.puml core_classes_updated.puml
ren packages.puml core_packages_updated.puml
