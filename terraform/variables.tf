variable "prefix" {
  type    = string
  default = "devopsproj"
}

variable "location" {
  type    = string
  default = "eastus"
}

variable "resource_group_name" {
  type    = string
  default = "${var.prefix}-rg"
}

variable "acr_sku" {
  type    = string
  default = "Standard"
}

variable "aks_node_count" {
  type    = number
  default = 2
}

variable "aks_node_vm_size" {
  type    = string
  default = "Standard_DS2_v2"
}
