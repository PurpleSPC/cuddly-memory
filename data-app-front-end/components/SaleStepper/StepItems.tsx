"use client"

import React, { useState } from "react";
import { SaleItem, initialSaleItems } from "@/app/schemas/saleItem";

interface StepItemsProps {
    saleID: number | null;
}

// 2nd step of SaleFormStepper
export default function StepItems({ saleID }: StepItemsProps) {
    const [items, setItems] = useState<SaleItem[]>(initialSaleItems);
    const [searchTerm, setSearchTerm] = useState("");

    const handleItemChange = (index: number, field: keyof SaleItem, value: number) => {
        const updatedItems = [...items];
        updatedItems[index] = { ...updatedItems[index], [field]: value };
        
        // Auto-calculate line total
        if (field === 'qty' || field === 'unitPrice') {
            const qty = updatedItems[index].qty || 0;
            const unitPrice = updatedItems[index].unitPrice || 0;
            updatedItems[index].lineTotal = qty * unitPrice;
        }
        
        setItems(updatedItems);
    };

    const addItem = () => {
        setItems([...items, { saleID: saleID || 0, productID: 0, qty: 0, unitPrice: 0, lineTotal: 0 }]);
    };

    const removeItem = (index: number) => {
        if (items.length > 1) {
            setItems(items.filter((_, i) => i !== index));
        }
    };

    const totalAmount = items.reduce((sum, item) => sum + (item.lineTotal || 0), 0);

    return (
        <div className="space-y-6">
            <div className="flex justify-between items-center">
                <h3 className="text-lg font-semibold">Sale Items</h3>
                <button
                    onClick={addItem}
                    className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-accent transition-colors"
                >
                    Add Item
                </button>
            </div>

            {/* Search Bar */}
            <div className="relative">
                <input
                    type="text"
                    placeholder="Search products by catalog # or description..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent"
                />
            </div>

            {/* Items Table */}
            <div className="overflow-x-auto">
                <table className="w-full border-collapse border border-gray-200">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="border border-gray-200 px-4 py-2 text-left">Catalog #</th>
                            <th className="border border-gray-200 px-4 py-2 text-left">Description</th>
                            <th className="border border-gray-200 px-4 py-2 text-center">Qty</th>
                            <th className="border border-gray-200 px-4 py-2 text-center">Unit Price</th>
                            <th className="border border-gray-200 px-4 py-2 text-center">Line Total</th>
                            <th className="border border-gray-200 px-4 py-2 text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {items.map((item, index) => (
                            <tr key={index} className="hover:bg-gray-50">
                                <td className="border border-gray-200 px-4 py-2">
                                    <input
                                        type="number"
                                        value={item.productID || ''}
                                        onChange={(e) => handleItemChange(index, 'productID', parseInt(e.target.value) || 0)}
                                        className="w-full px-2 py-1 border border-gray-300 rounded focus:ring-1 focus:ring-primary"
                                        placeholder="Product ID"
                                    />
                                </td>
                                <td className="border border-gray-200 px-4 py-2">
                                    <span className="text-gray-600">Product description will appear here</span>
                                </td>
                                <td className="border border-gray-200 px-4 py-2">
                                    <input
                                        type="number"
                                        min="0"
                                        max="99"
                                        value={item.qty || ''}
                                        onChange={(e) => handleItemChange(index, 'qty', parseInt(e.target.value) || 0)}
                                        className="w-20 px-2 py-1 border border-gray-300 rounded focus:ring-1 focus:ring-primary text-center"
                                    />
                                </td>
                                <td className="border border-gray-200 px-4 py-2">
                                    <input
                                        type="number"
                                        step="0.01"
                                        min="0"
                                        value={item.unitPrice || ''}
                                        onChange={(e) => handleItemChange(index, 'unitPrice', parseFloat(e.target.value) || 0)}
                                        className="w-24 px-2 py-1 border border-gray-300 rounded focus:ring-1 focus:ring-primary text-center"
                                    />
                                </td>
                                <td className="border border-gray-200 px-4 py-2 text-center font-medium">
                                    ${(item.lineTotal || 0).toFixed(2)}
                                </td>
                                <td className="border border-gray-200 px-4 py-2 text-center">
                                    <button
                                        onClick={() => removeItem(index)}
                                        disabled={items.length === 1}
                                        className={`px-3 py-1 rounded text-sm ${
                                            items.length === 1
                                                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                                                : 'bg-red-100 text-red-600 hover:bg-red-200'
                                        }`}
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            {/* Total */}
            <div className="flex justify-end">
                <div className="text-lg font-semibold">
                    Total Amount: <span className="text-primary">${totalAmount.toFixed(2)}</span>
                </div>
            </div>
        </div>
    );
}



    // 	catalog #: search by catalog# or description, autoupdate
	// qty: integer picker
	// unit_price: default to be looked up in db, editable

    // table or grid for inputs
    // need calculated line totals and overall total

    // use useFieldArray() from React Hook Form????