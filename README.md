# Retail Maintenance Management System

[English](README.md) | [Português](README.pt-BR.md)

A Python-based application designed to simulate maintenance management across  large supermarket network.

The project applies Object-Oriented Programming concepts to represent stores, maintenance orders, budgets, costs, operational history, and different business rules for preventive, corrective, and emergency maintenance.

> **Disclaimer:** This project is entirely fictional and was developed exclusively for educational and portfolio purposes. It does not represent the systems, processes, data, or operations of any real company.

---

## Overview

Large retail networks operate multiple stores and depend on different types of infrastructure and equipment to maintain daily operations.

Maintenance activities may involve electrical systems, refrigeration, air conditioning, hydraulic systems, equipment, facilities, and other operational assets.

In this fictional scenario, the objective was to develop an application capable of organizing and controlling maintenance orders across multiple supermarket locations.

The system supports three maintenance categories:

- Preventive Maintenance
- Corrective Maintenance
- Emergency Maintenance

Each maintenance type follows its own rules for budget usage and cost registration.

---

## Business Problem

A large supermarket network may need to manage several maintenance activities simultaneously across different stores.

Without a structured process, some common challenges may include:

- difficulty tracking maintenance orders by store;
- limited visibility into maintenance budgets and costs;
- different priority levels depending on the maintenance type;
- lack of centralized maintenance history;
- difficulty applying consistent business rules across multiple locations.

This project simulates how this operational process can be represented through a Python application using Object-Oriented Programming.

---

## Project Objective

The objective of this project is to build an application capable of:

- registering supermarket stores;
- creating maintenance orders;
- associating maintenance orders with specific stores;
- classifying maintenance as preventive, corrective, or emergency;
- adding budgets to maintenance orders;
- registering maintenance costs;
- tracking available budget;
- maintaining an operational history;
- handling invalid operations using custom exceptions.

---

## Maintenance Types

### Preventive Maintenance

Represents planned maintenance activities intended to reduce the likelihood of failures.

Registered costs must remain within the available maintenance budget.

### Corrective Maintenance

Represents interventions performed after a problem or failure has been identified.

In this fictional scenario, corrective maintenance can use the available budget plus an additional contingency limit.

### Emergency Maintenance

Represents critical situations that may directly affect store operations and require immediate intervention.

In this fictional scenario, emergency maintenance orders include an additional limit to support urgent operational costs.

---

## Object-Oriented Programming Concepts

The project was structured to apply important OOP concepts.

### Abstraction

`MaintenanceOrder` acts as an abstract base class that defines common behavior for all maintenance orders.

### Inheritance

Specific maintenance types inherit from the base class:

```text
MaintenanceOrder
├── PreventiveMaintenanceOrder
├── CorrectiveMaintenanceOrder
└── EmergencyMaintenanceOrder
```

### Polymorphism

Each maintenance type implements its own cost registration rules.

The same operation:

```python
order.register_cost(value)
```

can behave differently depending on the maintenance type.

### Encapsulation

Internal attributes such as budget, order ID, store reference, and operational history are controlled by the application classes.

### Composition

The supermarket network contains stores and maintenance orders.

Each store can also contain multiple associated maintenance orders.

---

## Application Workflow

```text
Supermarket Network
        │
        ▼
Register Store
        │
        ▼
Create Maintenance Order
        │
        ├── Preventive
        ├── Corrective
        └── Emergency
        │
        ▼
Add Budget
        │
        ▼
Register Costs
        │
        ▼
Track Available Budget
        │
        ▼
View Maintenance History
```

---

## Application Interface

The current version uses a Command-Line Interface (CLI).

Example of the main menu:

```text
--- Retail Maintenance Management System ---

1. Add Store
2. Create Maintenance Order
3. Access Maintenance Order
4. Exit

Choose an option:
```

When accessing a maintenance order:

```text
--- Maintenance Order Nº 1 ---

Store: Paulista Store
Available Budget: R$5000.00

1. Add Budget
2. Register Cost
3. View History
4. Return to Main Menu
```

---

## Project Structure

```text
retail_maintenance_management/
│
├── entities/
│   ├── __init__.py
│   ├── store.py
│   └── maintenance.py
│
├── operations/
│   ├── __init__.py
│   └── network.py
│
├── utils/
│   ├── __init__.py
│   └── exceptions.py
│
├── images/
│   ├── main_menu.png
│   ├── maintenance_order.png
│   └── maintenance_history.png
│
├── main.py
├── README.md
├── README.pt-BR.md
├── requirements.txt
└── .gitignore
```

---

## Technologies and Concepts

- Python
- Object-Oriented Programming
- Abstract Classes
- Inheritance
- Polymorphism
- Encapsulation
- Composition
- Custom Exceptions
- Command-Line Interface

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Guid3Paula/retail_maintenance_management.git
```

Navigate to the project directory:

```bash
cd retail_maintenance_management
```

Run the application:

```bash
python main.py
```

---

## Example Scenario

A fictional supermarket store is registered:

```text
Store: Paulista Store
Store ID: 001
```

A maintenance order is then created for that store.

An initial budget can be added:

```text
R$ 5,000.00
```

Maintenance costs can then be registered and the available budget is updated accordingly.

Each operation is stored in the maintenance order history with its corresponding date and time.

---

## Application Screenshots

### Main Menu

![Main Menu](images/main_menu.png)

### Maintenance Order

![Maintenance Order](images/maintenance_order.png)

### Maintenance History

![Maintenance History](images/maintenance_history.png)

---

## Future Improvements

Possible future developments include:

- graphical user interface;
- web application using Streamlit;
- database persistence;
- maintenance status tracking;
- technician management;
- supplier management;
- equipment and asset registration;
- SLA management;
- preventive maintenance scheduling;
- operational dashboards;
- cost analysis by store;
- maintenance performance indicators.

---

## Conclusion

This project demonstrates how Object-Oriented Programming concepts can be used to translate an operational business problem into structured software components.

More than simply implementing Python classes, the objective was to represent entities, responsibilities, behaviors, and business rules within an application.

The current command-line version provides a foundation that can later evolve into graphical interfaces, databases, automation workflows, and operational analytics.

---

## Disclaimer

All companies, stores, maintenance scenarios, budgets, costs, and operational rules presented in this project are fictional.

The project was developed exclusively for educational and portfolio purposes and does not represent any real company or internal business process.