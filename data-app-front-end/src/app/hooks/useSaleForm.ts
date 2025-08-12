import { useState } from "react";
import { useForm } from "./useForm";
import { BasicSaleInfo, initialBasicSaleInfo, saleSchema } from "../schemas/basicSaleInfo";
import { SaleItem, saleItemSchema, initialSaleItems, saleItemArraySchema } from "../schemas/saleItem";
import {z} from "zod"


// Basic Info
export function useSaleForm() {
  const today = new Date().toISOString().slice(0,10);
  const [saleID, setSaleID] = useState<number | null>(null);
  const [step, setStep] = useState<number>(0);

  const saleItemsForm = useForm<SaleItem[]>({ ... });


  const handleItemChange = (
    index: number,
    field: keyof SaleItem,
    value: number,
  ) => {
    const updatedItems = [...saleItemsForm.values];
    updatedItems[index][field] = value;

    const qty = updatedItems[index].qty ?? 0;
    const unitPrice = updatedItems[index].unitPrice ?? 0;
    updatedItems[index].lineTotal = qty * unitPrice;

    saleItemsForm.setValues(updatedItems);
  };


  const basicInfoForm = useForm<BasicSaleInfo>({
    initialValues: initialBasicSaleInfo,
    schema: saleSchema,
    onSubmit: async (values) => {
      const res = await fetch('http://localhost:8000/sales/create', {
          method: "POST",
          headers: { "Content-Type": "application/json"},
          body: JSON.stringify(values)
      });

      const data = await res.json();
      setSaleID(data.saleID);
      setStep(1);
    },
  });

  

// Adding Sale Items

  const nextStep = () => setStep((s) => Math.min(s + 1, 2));
  const prevStep = () => setStep((s) => Math.max(S -1,0));

  return {
    step,
    nextStep,
    prevStep,
    saleID,
    basicInfoForm,
    saleItemsForm,
    saleItemsForm,
    handleItemChange
  };

}