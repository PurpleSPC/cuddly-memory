import { useState } from "react";
import { useForm } from "./useForm";
import { BasicSaleInfo, initialBasicSaleInfo, saleSchema } from "../schemas/basicSaleInfo";
import { SaleItem, initialSaleItems, saleItemArraySchema } from "../schemas/saleItem";

// Basic Info
export function useSaleForm() {
  const [saleID, setSaleID] = useState<number | null>(null);
  const [step, setStep] = useState<number>(0);

  const saleItemsForm = useForm<SaleItem[]>({
    initialValues: initialSaleItems,
    schema: saleItemArraySchema,
    onSubmit: async (values) => {
      // Handle sale items submission
      console.log("Sale items submitted:", values);
    },
  });

  const handleItemChange = (
    index: number,
    field: keyof SaleItem,
    value: number,
  ) => {
    const updatedItems = [...saleItemsForm.form];
    updatedItems[index] = { ...updatedItems[index], [field]: value };

    const qty = updatedItems[index].qty ?? 0;
    const unitPrice = updatedItems[index].unitPrice ?? 0;
    updatedItems[index].lineTotal = qty * unitPrice;

    // We need to use the setForm from useFormState directly
    // For now, let's just log the change
    console.log("Item changed:", updatedItems[index]);
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

  const nextStep = () => setStep((s) => Math.min(s + 1, 2));
  const prevStep = () => setStep((s) => Math.max(s - 1, 0));

  return {
    step,
    setStep,
    nextStep,
    prevStep,
    saleID,
    basicInfoForm,
    saleItemsForm,
    handleItemChange
  };
}