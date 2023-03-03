#!/bin/bash

bandera = true

elements = ()

while $bandera; do
	echo "que deseas agregar a tu lista o presiona s para salir"
	read element

	if [[ $element != "s" ]]; then
		elemens+=($element)
	else
		
done
