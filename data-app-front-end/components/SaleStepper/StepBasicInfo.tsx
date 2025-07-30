"use client"

import FormField from "../Forms/FormField";
import FormPage from "../Forms/FormPage";
import { useForm } from "@/app/hooks/useForm";
import { schemaCreate } from "../../lib/schemaCreate";
import FieldRenderer from "../Forms/FormFieldRenderer";
import { z } from "zod"


interface BasicSaleInfo {  // TODO: will need to transition to a formatted id
    saleDate: string;  // how do JS dates work again?
    receivedDate: string;  // oh yeah, i have to convert from UTC to yyyy-mm-dd
    accountID: number; 
    productLineID: number;
    surgeonID: number;
    repID: number;
    rstckLocID: number;
}


// create validation schema
const schema = z.object({       // TODO: use z.string.regex for custom format
    saleDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, {
        message: "Date must be in YYYY-MM-DD format",
    }),
    receivedDate: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, {
        message: "Date must be in YYYY-MM-DD format",
    }),
    accountID: z.number({message: "Invalid Account ID format"}),
    productLineID: z.number({message: "Invalid Product Line format"}),
    surgeonID: z.number({message: "Invalid Surgeon ID format"}),
    repID: z.number({message: "Invalid RepID format"}),
    rstckLocID: z.number({message:"Invalid Restock Loc ID format"}),
})




// first step in SaleFormStepper
export default function StepBasicInfo() {
    const today = new Date().toISOString().slice(0,10);
    const {
        form,
        handleSubmit,
        errors,
        isSubmitting,
        success,
        error,
        handleChange,
    } = useForm<BasicSaleInfo>({
        initialValues: {
            saleDate: today,
            receivedDate: today,
            accountID: 0,
            productLineID: 0,
            surgeonID: 0,
            repID: 0,
            rstckLocID: 0
        },
        schema,
        onSubmit: async(formData) => {
            await fetch("http://localhost:8000/sales/create", {
                method:"POST",
                headers:{"Content-Type": "application/json"},
                body: JSON.stringify(formData),
            });       
        },

    });

    const fieldConfigs = schemaCreate(schema)
    return (
        <FormPage
            title = "Basic Sale Info"
            onSubmit={handleSubmit}
            loading={isSubmitting}
            success={success}
            error={error}
            successText="Sale Created"
            errorText="Sale not created. try again"
            >
            <FieldRenderer<BasicSaleInfo>
                fields={fieldConfigs}
                values={form}
                errors={errors}
                onChange={handleChange}
                />

        </FormPage>
    // account: select or search from account names, have a "new account" button that opens create-account in modal
    // product_line: select or search
    // surgeon: select or search. have a "new surgeon" button that opens create-surgeon in modal
    // rep_id: select or search
    // rstck_loc: int = select or search
    // hasPo?: boolean conditionally renders PO# field


    // useValidation from zod for validation

    // modal triggers for new accounts or surgeons
    );
}