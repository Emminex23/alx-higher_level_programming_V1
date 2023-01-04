#include <Python.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_list - Prints basic info about a Python list object
 * @p: Pointer to the Python list object
 *
 * Return: Always 0
 */
void print_python_list(PyObject *p)
{
    int i;
    Py_ssize_t size;
    PyObject *item;

    if (!PyList_Check(p))
    {
        puts("Invalid List Object");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
    }
}

/**
 * print_python_bytes - Prints basic info about a Python bytes object
 * @p: Pointer to the Python bytes object
 *
 * Return: Always 0
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t i;

    if (!PyBytes_Check(p))
    {
        puts("Invalid Bytes Object");
        return;
    }

    size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    if (size > 9)
    {
        puts("  first 10 bytes:");
        for (i = 0; i < 10; i++)
        {
            printf("%02hhx%c", PyBytes_AsString(p)[i], i + 1 < 10 ? ' ' : '\n');
        }
    }
    else
    {
        puts("  first X bytes:");
        for (i = 0; i < size; i++)
        {
            printf("%02hhx%c", PyBytes_AsString(p)[i], i + 1 < size ? ' ' : '\n');
        }
    }
}
