#include <Python.h>
#include <stdio;h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    string = ((PyBytesObject *)(p))->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    if (size >= 10)
        printf("  first 10 bytes:");
    else
        printf("  first %ld bytes:", size + 1);

    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", string[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *obj;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
        return;

    size = ((PyVarObject *)(p))->ob_size;
    allocated = ((PyListObject *)(p))->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        obj = ((PyListObject *)(p))->ob_item[i];
        printf("Element %ld: %s\n", i, obj->ob_type->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}
