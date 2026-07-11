#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints structural details about CPython list elements
 * @p: PyObject representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, allocated, i;
	PyObject *item;

	list_size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
