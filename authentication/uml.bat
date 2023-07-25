pyreverse --output puml --colorized -A --output-directory authentication authentication
python -m plantuml packages.puml
python -m plantuml classes.puml
ren classes.png authentication_classes_updated.png
ren packages.png authentication_packages_updated.png
ren classes.puml authentication_classes_updated.puml
ren packages.puml authentication_packages_updated.puml
