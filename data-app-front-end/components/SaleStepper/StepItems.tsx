"use client"

import FormPage from "../Forms/FormPage";
import { useForm } from "@/app/hooks/useForm";
import FieldRenderer from "../Forms/FormFieldRenderer";
import { SaleItem, fieldConfigs, initialSaleItems, saleItemSchema } from "@/app/schemas/saleItem";
import { useSaleForm } from "@/app/hooks/useSaleForm";


// 2nd step of SaleFormStepper

export default function StepItems() {
    // const {
    //     form,
    //     handleSubmit,
    //     errors,
    //     isSubmitting,
    //     success,
    //     error,
    //     handleChange,
    // } = useForm<SaleItem>({
    //     initialValues: initialSaleItems,
    //     schema: saleItemSchema,
    //     onSubmit: async(formData) => {
    //         await fetch("http://localhost:8000/sales/add", {
    //             method:"POST",
    //             headers:{"Content-Type": "application/json"},
    //             body: JSON.stringify(formData),
    //         }); 
    //     },
    // });
    
    const { saleItemsForm, handleItemChange } = useSaleForm();
    
    return (
        <FormPage
            title = "Add Sale Items"
            {saleItemsForm}
            >
            

        </FormPage>
        
    );
}



    // 	catalog #: search by catalog# or description, autoupdate
	// qty: integer picker
	// unit_price: default to be looked up in db, editable

    // table or grid for inputs
    // need calculated line totals and overall total

    // use useFieldArray() from React Hook Form????